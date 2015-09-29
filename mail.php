<?
//include('Mail.php');
//include('Mail/mime.php');
//// Constructing the email
//$sender = "akhilraj.app@gmail.com";
//$recipient = "Akhilraj <akhilrajns@gmail.com>";
//$subject = "Test Email";
//$text = 'This is a text message.';
//$html = '<html><body><p>This is a html message</p></body></html>';
//$crlf = "\n";
//$headers = array(
//'From'          => $sender,
//'Return-Path'   => $sender,
//'Subject'       => $subject
//);
//// Creating the Mime message
//$mime = new Mail_mime($crlf);
//// Setting the body of the email
//$mime->setTXTBody($text);
//$mime->setHTMLBody($html);
// // Set body and headers ready for base mail class
//$body = $mime->get();
//$headers = $mime->headers($headers);
//
//
// $host = "smtp.gmail.com";
// $port = "587";
// $username = "akhilraj.app@gmail.com";
// $password = "***********";
//
//
//// SMTP params
// $mail = Mail::factory('smtp',
//   array ('host' => $host,
//     'port' => $port,
//     'auth' => true,
//     'username' => $username,
//     'password' => $password));
//
//
//// Sending the email using smtp
//$result = $mail->send($recipient, $headers, $body);
//if($result == 1)
//{
//echo("Your message has been sent!".$result);
//}
//else
//{
//echo("Your message was not sent: " . $result);
//}

$output = exec("cd /var/www/myapptest/& python mail.python.py ");

echo "<pre>";print_r($output);
?>
