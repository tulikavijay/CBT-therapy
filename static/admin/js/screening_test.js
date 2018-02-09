$('button').on('click',function(){
  var score = [];
  for(i=1;i<=7;i++){
    let t = document.getElementsByName(String(i));
    t.forEach(radio=>{if(radio.checked) score.push(radio.value)});
  }
  console.log(score);
});
