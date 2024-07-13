from pydantic import BaseModel, Field
from typing import Annotated


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Joao',
                               max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900',
                               max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Idade do atleta', examples='25')]
