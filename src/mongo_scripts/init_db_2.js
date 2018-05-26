//use alphacar;

load("lib/base_operation.js");
BO = new BaseOperation();
let database = BO.getDB();

database.dropDatabase();

database.alphacar.insert({"name": "AlphaCar"});

print(database.alphacar.find());
