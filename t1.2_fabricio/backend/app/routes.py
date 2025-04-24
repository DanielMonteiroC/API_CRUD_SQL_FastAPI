from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

@router.get("/itens/", response_model=list[schemas.ItemOut])
def listar_itens(db: Session = Depends(database.get_db)):
    return crud.get_itens(db)

@router.get("/itens/{item_id}", response_model=schemas.ItemOut)
def obter_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return db_item

@router.post("/itens/", response_model=schemas.ItemOut)
def criar_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, item)

@router.put("/itens/{item_id}", response_model=schemas.ItemOut)
def atualizar_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(database.get_db)):
    return crud.update_item(db, item_id, item)

@router.delete("/itens/{item_id}")
def deletar_item(item_id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db, item_id)
    return {"mensagem": "Item deletado com sucesso"}