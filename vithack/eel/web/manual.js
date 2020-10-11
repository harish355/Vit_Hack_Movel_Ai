function left()
{
    eel.left()//(change)
}
function right()
{
    eel.right()//(change)
}
function up()
{
    eel.up()//(change)
}
function down()
{
    eel.down()//(change)
}


// function change(ret)
// {
    
//     var data=document.getElementById("hist").innerHTML;
    
// //     if(data.toString()=="Switching control to joystick")
// //     {
        
// //     document.getElementById("hist").innerHTML=data+ret+'<br>';
// //     alert("control changed \n"+ret);
// // }
// //     else
// //     {
//         document.getElementById("hist").innerHTML=ret+'<br>';
//         // alert(ret);
//     // }
    
// }
function joystick()
{
    eel.joystick()(function (ret)
    {
        // document.getElementById("hist").innerHTML=ret+'<br>'
    alert(ret)
    })
}
