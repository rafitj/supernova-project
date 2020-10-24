$(document).ready(() => {
    var content = ""
    for (let i = 0; i < 50; i++) {
        content += "<tr>"
        for (let j = 0; j < 100; j++) {
            content += `<td id=x${j}y${i}></td>`
        }
        content += "</tr>"
    }
    $("#field").append(content)
})

const resetField = () => {
    for (let i = 0; i < 50; i++) {
        for (let j = 0; j < 100; j++) {
            $(`#x${j}y${i}`).removeClass()
        }
    }
}

const colorCell = (x, y, color) => {
    $(`#x${x}y${y}`).addClass(color)
}

const updateField = (data) => {
    resetField()
    console.log(data.ball)
    colorCell(data.ball[0], data.ball[1], 'black');
    data.team_a.forEach(coord => {
        colorCell(coord[0], coord[1], 'red');
    });
    data.team_b.forEach(coord => {
        colorCell(coord[0], coord[1], 'blue');
    });
}