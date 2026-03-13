from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationResponse
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=OrganizationResponse)
def create_org(
    org: OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_org = Organization(
        name=org.name,
        owner_id=current_user.id
    )

    db.add(new_org)
    db.commit()
    db.refresh(new_org)

    return new_org