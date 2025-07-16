# from db.mongodb.client import MongoDBClient
# from schemas.invoice_log import InvoiceLogResponse
# from typing import List


# class InvoiceLogRepository:
#     def __init__(self, client: MongoDBClient):
#         self.client = client
#         self.collection = client.get_collection("invoice_logs")

#     def get_all(self) -> List[InvoiceLogResponse]:
#         docs = list(self.collection.find({}))
#         return [InvoiceLogResponse(**doc) for doc in docs]
