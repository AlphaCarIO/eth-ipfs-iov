var mongoose = require('mongoose');
var bluebird = require('bluebird');

mongoose.Promise=bluebird;

import * as config from "../config/config"
import * as cc from "../config/constants"

mongoose.connect(cc.mongodb_url);
