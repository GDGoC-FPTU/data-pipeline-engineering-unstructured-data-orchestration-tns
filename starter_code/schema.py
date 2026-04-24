from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    """
    document_id: str = Field(..., description="Unique document identifier")
    source_type: str = Field(..., description="Source system/type of the document")
    author: str = Field(..., description="Author or creator of the document")
    category: str = Field(..., description="Document category")
    content: str = Field(..., description="Main textual content")
    timestamp: str = Field(..., description="Document timestamp")
