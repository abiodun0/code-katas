function repeatString( s , n )
{
  return n ? new Array( n + 1 ).join( s ) : "";
}

function getDecentNumber( n )
{
    var threes = 0,
        fives  = 0,
        remainingDigits = +n;
    while (remainingDigits > 2) {
        if (remainingDigits % 3 === 0) {
            fives = remainingDigits;
            break;
        }
        remainingDigits -= 5;
    }
    threes = n - fives;
    if (remainingDigits < 0 || threes % 5)
        return "-1";

    return repeatString( '5', fives ) + repeatString( '3', threes );
}

console.log(getDecentNumber(90));