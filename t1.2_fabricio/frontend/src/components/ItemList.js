import React from "react";
import api from "../api";

function ItemList({ itens, fetchItems }) {
  const deletar = async (id) => {
    await api.delete(`/itens/${id}`);
    fetchItems();
  };

  return (
    <ul>
      {itens.map((item) => (
        <li key={item.id}>
          <strong>{item.nome}</strong> - {item.descricao}
          <button onClick={() => deletar(item.id)}>Excluir</button>
        </li>
      ))}
    </ul>
  );
}

export default ItemList;
