<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <head>
        <title>  <?php echo 'home';?></title>
    </head>
    <body>


        <div style="width: 500px;height: 500px;border: 1px solid red; margin: 20 auto">


      <div id="fb-root"></div>
      <script src="http://connect.facebook.net/en_US/all.js">
      </script>
      <script>
         FB.init({
            appId:'YOUR_APP_ID', cookie:true,
            status:true, xfbml:true
         });

         FB.ui({ method: 'feed',
            message: 'Facebook for Websites is super-cool'});
      </script>



           </div>
<?php echo "HOME";?>



<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1&appId=159480090762229";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
    </body>
</html>