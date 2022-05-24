function addRow(){
    var id = document.getElementById("id");
    var name = document.getElementById("name");
    var qtde = document.getElementById("qtde");
    var un = document.getElementById("un");

    var table = document.getElementById("myTableData");

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    row.insertCell(0).innerHTML = id.value + '<input type="hidden" name="TDIngrediente.id.'+id.value+'" value="'+id.value +'">';
    row.insertCell(1).innerHTML = name.value + '<input type="hidden" name="TDIngrediente.name.'+id.value+'" value="'+name.value +'">';
    row.insertCell(2).innerHTML = qtde.value + '<input type="hidden" name="TDIngrediente.qtde.'+id.value+'" value="'+qtde.value +'">';
    row.insertCell(3).innerHTML = un.value + '<input type="hidden" name="TDIngrediente.un.'+id.value+'" value="'+un.value +'">';
    row.insertCell(4).innerHTML = '<input type="button" value = "Delete" onClick="Javacsript:deleteRow(this)">';
}

function deleteRow(obj){
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myTableData");
    table.deleteRow(index);
}


function load(){
    console.log("Page load finished");
}