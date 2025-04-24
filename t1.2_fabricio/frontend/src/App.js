import React, { useEffect, useState } from "react";
import api from "./api";
import ItemForm from "./components/ItemForm";
import ItemList from "./components/ItemList";

function App() {
  const [itens, setItens] = useState([]);

  const fetchItems = async () => {
    const res = await api.get("/itens/");
    setItens(res.data);
  };

  useEffect(() => {
    fetchItems();
  }, []);

  return (
    <div>
      <h1>Lista de Itens</h1>
      <ItemForm fetchItems={fetchItems} />
      <ItemList itens={itens} fetchItems={fetchItems} />
    </div>
  );
}

export default App;
