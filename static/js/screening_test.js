$(document).ready(function(e){
  const forms=document.querySelectorAll(`form`);
   form.addEventListener('submit',rate);
   var rate='';
   var cat='';
   var page='';
   $(`input[type=radio]`).on('click',function(){

     console.log(this);
      rate=$(this).val();
      cat=$(this).attr("data-cat");
      page=$(this).attr("data-page");
      console.log(rate)
      $(this).closest("form").submit();

   });
   function rate(){
      e.preventDefault();
      console.log(rate);

        $.ajax({
          type:'POST',
          url:'/rate/',
          data:{
            category_name:cat,
            page:page,
            rate:rate,
            csrfmiddlewaretoken:$(`input[name=csrfmiddlewaretoken]`).val()
          },
          sucess: function(){
            $('.desc').html(data);
          }
        });
        e.preventDefault();
   }
});
