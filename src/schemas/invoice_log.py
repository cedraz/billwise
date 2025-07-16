from pydantic import BaseModel, ConfigDict
import datetime
from typing import List


class Change(BaseModel):
    field: str
    old_value: str
    new_value: str


class InvoiceLogResponse(BaseModel):
    user_id: int
    date: datetime
    changes: List[Change]

    model_config = ConfigDict(arbitrary_types_allowed=True)


def individual_data(invoice_log: dict):
    return {
        "user_id": invoice_log["user_id"],
        "date": invoice_log["date"],
        "changes": [
            {
                "field": change["field"],
                "old_value": change["old_value"],
                "new_value": change["new_value"]
            }
            for change in invoice_log["changes"]
        ]
    }


def all_invoice_logs(invoice_logs):
    return [individual_data(log) for log in invoice_logs]
