$Username = "@gmail.com";
$Password = "";

function Send-ToEmail([string]$email, [string]$attachmentpath){

    $message = new-object Net.Mail.MailMessage;
    $message.From = "myemail@gmail.com";
    $message.To.Add($email);
    $message.Subject = "subject text here...";
    $message.Body = "body text here...";
    $attachment = New-Object Net.Mail.Attachment($attachmentpath);

    $smtp = new-object Net.Mail.SmtpClient("smtp.gmail.com", "587");
    $smtp.EnableSSL = $true;
    $smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password);
    $smtp.send($message);
    write-host "Mail Sent" ; 
    $attachment.Dispose();
 }
Send-ToEmail  -email "myemail@gmail.com" -attachmentpath $path;
