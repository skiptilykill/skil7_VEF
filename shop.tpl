<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>VEFverslun</title>
</head>
<body>

    <h2>Veldu vöru</h2>
    <table border="1">
        <tr>
            <th>Vöruheiti</th>
            <th>Verð</th>
        </tr>
        % for p in products:
            <tr>
                <td><a href="/cart/add/{{p['pid']}}">{{p['name']}}</a></td>
                <td>{{p['price']}}</td>
            </tr>
         % end
    </table>

    <p><a href="/cart">Sjá Körfu</a></p>
    <p><a href="/">Til baka</a></p>

</body>
</html>