from pydantic import BaseModel, Field
from typing import Optional

class Plague(BaseModel):

    id: Optional[int] = Field(None, description="Уникальный идентификатор болезни", example=1)
    name: str = Field(..., description="Название пользовательской болезни", example="T-вирус")
    type: str = Field(..., description="Тип болезни", example="Вирус")
    lethality: int = Field(..., ge=0, le=100, description="летальность болезни в процентах", example=10)
    incubation_period: int = Field(..., ge=1, le=1825, description="Период инкубации в днях", example= 2)
    is_vaccine: bool = Field(False, description="Существует ли вакцина")
    image: str = Field(..., description="Изображение под микроскопом", example="static/images/t_virus.jpg")
    description: Optional[str] = Field(None, description="Описание болезни")