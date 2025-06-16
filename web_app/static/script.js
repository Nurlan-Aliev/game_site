function moveToRoom(thisRoom, nextRoom) {

    fetch(`/change_room?this_room=${thisRoom}&next_room=${nextRoom}`, {
        method: 'GET',
    })
        .then(response => response.text())
        .then(html => {
            document.getElementById("game-container").innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}



function attackMonster(thisRoom, myAttack) {
console.log(thisRoom)

    fetch(`/fight?room=${thisRoom}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            attack: myAttack
        })
    })
        .then(response => response.text())
        .then(html => {
            document.getElementById("game-container").innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}