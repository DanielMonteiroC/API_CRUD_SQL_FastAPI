import React, { useState } from "react";
import api from "../api";

function ItemForm({ fetchItems }) {
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post("/itens/", { nome, descricao });
    setNome("");
    setDescricao("");
    fetchItems();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={nome} onChange={(e) => setNome(e.target.value)} placeholder="Nome" />
      <input value={descricao} onChange={(e) => setDescricao(e.target.value)} placeholder="Descrição" />
      <button type="submit">Adicionar</button>
    </form>
  );
}

export default ItemForm;
