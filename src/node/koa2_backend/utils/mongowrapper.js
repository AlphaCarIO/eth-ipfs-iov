var mongoose = require('mongoose');
var bluebird = require('bluebird');

//mongoose.Promise=bluebird;

import * as config from "../config/config"

/*

{
"ubi_code" : "1", 
"timestamp" : "1529989200", 
"start_date" : "2018-01-01", 
"end_date" : "2018-12-30", 
"user" : { "name" : "leo", "driving_license" : "12345" }, 
"car_info" : { "car_type" : "ford", "vin_code" : "123" }, 
"hash" : "QmQe1G371HqCzqYVaq9WfaLRyDRuLcUNEAXtS4GLyajLcW"
}

*/
let UBIInfo_Schema = new mongoose.Schema({
    //_id: {type: mongoose.Schema.Types.ObjectId},
    ubi_code: {type: String},
    timestamp: {type: Number, default: 0},
    start_date: {type: String},
    end_date: {type: String},
    user: { name: {type: String}, driving_license: {type: String}},
    car_info: { car_type: {type: String}, vin_code: {type: String}},
    hash: {type: String},
});

const options = {
    autoIndex: false, // Don't build indexes
    reconnectTries: Number.MAX_VALUE, // Never stop trying to reconnect
    reconnectInterval: 500, // Reconnect every 500ms
    poolSize: 10, // Maintain up to 10 socket connections
    // If not connected, return errors immediately rather than waiting for reconnect
    bufferMaxEntries: 0
  };

mongoose.connect(config.mongodb_url, options).then(
    () => { console.log('mongo connected!') },
    err => { console.log("connect err:", err) }
);

var UBIInfoModel = mongoose.model('ubi_info', UBIInfo_Schema, 'ubi_info');

//console.log('UBIInfo_Schema:', UBIInfo_Schema)
//console.log('UBIInfoModel:', UBIInfoModel)

module.exports = {
    mongoose,
    UBIInfoModel,
}
