import azure.functions as func
import json
import logging
from datetime import date

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


@app.route(route="payment_status", auth_level=func.AuthLevel.FUNCTION)
def payment_status(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing payment status request.")

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

        total_fee = float(row.TotalFee)
        paid_amount = float(row.PaidAmount)
        due_date = row.DueDate

        if paid_amount >= total_fee:
            status = "Paid"
        elif due_date < date.today():
            status = "Overdue"
        else:
            status = "Partially Paid"

        response = {
            "StudentID": row.StudentID,
            "TotalFee": total_fee,
            "PaidAmount": paid_amount,
            "DueDate": due_date.isoformat(),
            "PaymentStatus": status
        }

        return func.HttpResponse(
            json.dumps(response),
            status_code=200,
            mimetype="application/json"
        )

    except Exception:
        logging.exception("Error calculating payment status.")

        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error"
            }),
            status_code=500,
            mimetype="application/json"
        )


@app.route(
    route="update_fee",
    methods=["PUT"],
    auth_level=func.AuthLevel.FUNCTION
)
def update_fee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing admin fee update request.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({
                "error": "Invalid JSON request body"
            }),
            status_code=400,
            mimetype="application/json"
        )

    student_id = req_body.get("student_id")
    paid_amount = req_body.get("paid_amount")

    if not student_id:
        return func.HttpResponse(
            json.dumps({
                "error": "student_id is required"
            }),
            status_code=400,
            mimetype="application/json"
        )

    if paid_amount is None:
        return func.HttpResponse(
            json.dumps({
                "error": "paid_amount is required"
            }),
            status_code=400,
            mimetype="application/json"
        )

    try:
        paid_amount = float(paid_amount)

        if paid_amount < 0:
            return func.HttpResponse(
                json.dumps({
                    "error": "paid_amount cannot be negative"
                }),
                status_code=400,
                mimetype="application/json"
            )

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT TotalFee FROM Students WHERE StudentID = ?",
            student_id
        )

        row = cursor.fetchone()

        if row is None:
            cursor.close()
            connection.close()

            return func.HttpResponse(
                json.dumps({
                    "error": "Student not found"
                }),
                status_code=404,
                mimetype="application/json"
            )

        total_fee = float(row.TotalFee)

        if paid_amount > total_fee:
            cursor.close()
            connection.close()

            return func.HttpResponse(
                json.dumps({
                    "error": "Paid amount cannot exceed total fee"
                }),
                status_code=400,
                mimetype="application/json"
            )

        cursor.execute(
            """
            UPDATE Students
            SET PaidAmount = ?
            WHERE StudentID = ?
            """,
            paid_amount,
            student_id
        )

        connection.commit()

        cursor.close()
        connection.close()

        return func.HttpResponse(
            json.dumps({
                "message": "Fee updated successfully",
                "StudentID": student_id,
                "PaidAmount": paid_amount
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception:
        logging.exception("Error updating student fee.")

        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error"
            }),
            status_code=500,
            mimetype="application/json"
        )