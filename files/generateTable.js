/* This function generates the table in problem solutions.*/
function generateTable(dates){
    document.write("<table class=\"gradienttable\" width=\"50%\">");
    document.write("<tr><th>Date:</th><th>Problems:</th><th>Solutions:</th></tr>");
    for(var x = 0; x < dates.length; x++){
       document.write("<tr><td>", dates[x], "</td><td><a href =\"../solutions/COMCPS", 6-x, ".docx\" target=\"_blank\"> Click here. </a> </td><td><a href =\"../solutions/COMCSS", 6-x, ".docx\" target=\"_blank\"> Click here. </a> </td></tr>");
    }
    document.write("</table>");
}