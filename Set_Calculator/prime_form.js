


function removeDuplicates(list){
    var new_list = [];
    for (item in new_list){
        if ($.inArray(item, new_list) === -1){
            new_list.push(item);        
        }
    }
    return new_list
}

function copy(content){
    var j = document.getElementById("output");
    j.value = content;    
}

function businessLogic(input){ // this will eventually be findPrimeForm(set)
    input = input.split(",")
    return input[0]
    
}

function getResult(){
    this.output.value = businessLogic(
        this.input.value
        )
}