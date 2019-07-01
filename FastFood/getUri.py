def urify ( directory, denom ):
    denom = denom.lower();
    denom = denom.replace("'","");
    denom = denom.replace( "-", " "  );
    denom = denom.replace( "  ", " "  );
    denom = denom.replace( " ", "_"  );
    denom = denom.replace( "?", ""  );
    denom = denom.replace( "ù", "u"  );
    denom = denom.replace( "è", "e"  );
    denom = denom.replace( "é", "e"  );
    denom = denom.replace( "à", "a"  );
    denom = denom.replace( "ò", "o"  );
    denom = denom.replace( ">", ""  );
    denom = denom.replace( "<", ""  );
    denom = denom.replace( '"', ""  );
    denom = denom.replace( '.', ""  );
    denom = denom.replace( '/', "_"  );
    denom = denom.replace( ',', ""  );
    uri = "http://comune.milano.it/resource/" + directory +"/" + denom;
    return uri
