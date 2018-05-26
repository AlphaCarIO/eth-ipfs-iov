db.dropDatabase();

var todayDate = new Date().toISOString().slice(0, 10);

db.alphacar.insert({"name": "AlphaCar"});

db.createCollection(todayDate, { capped : false, autoIndexId : true } )

db.stats();

