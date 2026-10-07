import azure.functions as func
import json
import logging

from db import get_connection

app = func.FunctionApp()


@app.route(route="get_fee", auth_level=func.AuthLevel.FUNCTION)
def get_fee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing fee details request.")

    student_id = req.params.get("student_id")

    if not student_id:
        return func.HttpResponse(
            json.dumps({
                "error": "student_id is required"
            }),
            status_code=400,
            mimetype="application/json"
        )

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                StudentID,
                Name,
                Course,
                TotalFee,
                PaidAmount,
                DueDate
            FROM Students
            WHERE StudentID = ?
        """

        cursor.execute(query, student_id)
        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row is None:
            return func.HttpResponse(
                json.dumps({
                    "error": "Student not found"
                }),
                status_code=404,
                mimetype="application/json"
            )

        student = {
            "StudentID": row.StudentID,
            "Name": row.Name,
            "Course": row.Course,
            "TotalFee": float(row.TotalFee),
            "PaidAmount": float(row.PaidAmount),
            "DueDate": row.DueDate.isoformat()
        }

        return func.HttpResponse(
            json.dumps(student),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.exception("Error retrieving student fee details.")

        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error"
            }),
            status_code=500,
            mimetype="application/json"
        )