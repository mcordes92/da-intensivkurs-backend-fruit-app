async function fetchFruits() {
    const response = await fetch('http://127.0.0.1:8000/fruits/');
    const fruits = await response.json();
    const fruitList = document.getElementById('fruit-list');
    fruitList.innerHTML = '';
    fruits.forEach(fruit => {
        const row = document.createElement('tr');
        
        const nameCell = document.createElement('td');
        nameCell.textContent = fruit.name;
        row.appendChild(nameCell);
        
        const colorCell = document.createElement('td');
        colorCell.textContent = fruit.color;
        row.appendChild(colorCell);
        
        const weightCell = document.createElement('td');
        weightCell.textContent = fruit.weight;
        row.appendChild(weightCell);
        
        fruitList.appendChild(row);
    });
}
fetchFruits();