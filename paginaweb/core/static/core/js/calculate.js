var fechaInicio = document.getElementById("fechaInicio")
var fechaFin = document.getElementById("fechaFin")

var  today = new Date()
var tomorrow = new Date()
var sub_total_activities = 0
var adultos = 1
var menores = 0
var sub_total = 2
var last_day_value = 1
today.setDate(today.getDate() + 1)
tomorrow.setDate(today.getDate() + 1)

fechaInicio.value= convert(today)
fechaInicio.setAttribute("min", convert(today))
fechaFin.setAttribute("min", convert(tomorrow))

function changeFechaInicio(){
    if (fechaFin.value != ''){
        calculate()
    }
    tomorrow.setDate(new Date(fechaInicio.value).getDate() + 2)
    fechaFin.setAttribute("min", convert(tomorrow))
}

function changeFechaFin(){
     yesterday = new Date(fechaFin.value)
     fechaInicio.setAttribute("max", convert(yesterday))
     calculate()
}

function changeAdultos(){
    adultos = parseInt(document.getElementById("adultos").value)
    if (fechaFin.value == ''){
        tomorrow.setDate(new Date(fechaInicio.value).getDate() + 2)
        fechaFin.value= convert(tomorrow)
    }
    calculate()
}
function changeMenores(){
    menores =  parseInt(document.getElementById("menores").value)
    if (fechaFin.value == ''){
        tomorrow.setDate(new Date(fechaInicio.value).getDate() + 2)
        fechaFin.value= convert(tomorrow)
    }
    calculate()
}


function isSelected(value){
    cb = document.getElementById(value).checked
    if (fechaFin.value == ''){
        tomorrow.setDate(new Date(fechaInicio.value).getDate() + 2)
        fechaFin.value= convert(tomorrow)
        days = 1
    }
    amount = 0
    if (value == 'guia'){
        if(cb){
            sub_total_activities += 10
        }else{
            sub_total_activities -= 10
        }
     
    } else if (value == 'hospedaje'){
        amount = 7
    }
    else if (value == 'lancha'){
        if(cb){
            sub_total_activities +=7
        }else{
            sub_total_activities -= 7
        }
    
    }
    else if (value == 'salinas'){
        if(cb){
            sub_total_activities += 1
        }else{
            sub_total_activities -= 1
        }
    
    }
    else if (value == 'museo'){
        if(cb){
            sub_total_activities += 1
        }else{
            sub_total_activities -= 1
        }
     
    }
    else if (value == 'sendero'){
        if(cb){
            sub_total_activities += 1.50
        }else{
            sub_total_activities -= 1.50
        }
     
    }
    else if (value == 'carpas'){
        if(cb){
            sub_total_activities += 2
        }else{
            sub_total_activities -= 2
        }
    
    }
    
    if(sub_total < 0){
        sub_total=0
    }
    if (cb){
        sub_total += amount * days
    }else {
        sub_total -= amount * days
    }
    calculate()
}

function calculate(){
    days = (new Date(fechaFin.value) - new Date(fechaInicio.value))/(60*60*1000*24)
    sub_total = (sub_total / last_day_value)*days 
    last_day_value = days
    
    if (menores === 0){
        multiplier = adultos
    }else{
        multiplier = adultos + (menores/2)
    }
    preciofinal=(parseFloat(sub_total) +parseFloat(sub_total_activities))*parseFloat(multiplier)
    document.getElementById("days").innerHTML = 'Total Dias :' + days 
    document.getElementById("total").innerHTML = 'Precio Total :'+ (preciofinal)+ " $"
    document.getElementById("preciofinal").value = preciofinal
}

function convert(str) {
  var date = new Date(str),
    mnth = ("0" + (date.getMonth() + 1)).slice(-2),
    day = ("0" + date.getDate()).slice(-2);
  return [date.getFullYear(), mnth, day].join("-");
}