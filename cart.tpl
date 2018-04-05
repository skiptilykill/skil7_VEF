<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Cart</title>
</head>
<body>

    <h2>Karfan þín: </h2>

    %if len(karfa) <= 0:
        <p> Karfan er tóm.</p>
        <p><a href="/shop">Til baka</a></p>

    % else:
    %   for i in karfa:
            <p>{{i['vara']}} x {{i['fjoldi']}}</p>
    %   end
        <p><a href="/shop">Til baka</a></p>
    %end

<p><a href="/cart/remove">Tæma körfu</a></p>
</body>
</html>