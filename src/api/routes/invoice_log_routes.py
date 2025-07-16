from fastapi import APIRouter, status
from db.mongodb.client import invoice_log_collection
from schemas.invoice_log import all_invoice_logs
from db.mongodb.models.invoice_log import InvoiceLog
from fastapi import HTTPException

router = APIRouter(prefix="/invoice-logs", tags=["invoice-logs"])


@router.get("/")
async def get_all_invoice_logs():
    cursor = invoice_log_collection.find()
    data = cursor.to_list(length=100)  # Define um limite de documentos
    return all_invoice_logs(data)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_invoice_log(new_invoice_log: InvoiceLog):
    try:
        # ✅ Use .model_dump() para converter o objeto Pydantic e seus filhos em um dicionário puro
        invoice_log_dict = new_invoice_log.model_dump()

        result = invoice_log_collection.insert_one(invoice_log_dict)
        return {"id": str(result.inserted_id), "message": "Invoice log created successfully."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create invoice log: {str(e)}"
        )
