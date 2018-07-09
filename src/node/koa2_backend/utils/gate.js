var request = require('request');

const API_QUERY_URL = 'https://data.gateio.io/';
const PAIRS_URL = 'api2/1/pairs';
const MARKETINFO_URL = 'api2/1/marketinfo';
const MARKETLIST_URL = 'api2/1/marketlist';
const TICKERS_URL = 'api2/1/tickers';
const TICKER_URL = 'api2/1/ticker';
const ORDERBOOKS_URL = 'api2/1/orderBooks';
const ORDERBOOK_URL = 'api2/1/orderBook';
const TRADEHISTORY_URL = 'api2/1/tradeHistory';

const USER_AGENT = '';

const HEADERS = { 'User-Agent': USER_AGENT };

function Request (params, cp){
    request(params, function(error, response, body) {
        if(error) {
            cp(error);
        }else{
            cp(body);
        }
    });
}

var gate = {

    getPairs: function(cp) {
        Request({method: 'GET', url: API_QUERY_URL + PAIRS_URL, headers: HEADERS },cp);
    },

    getMarketinfo:function(cp) {
        Request({method: 'GET', url: API_QUERY_URL + MARKETINFO_URL, headers: HEADERS },cp);
    },

    getMarketlist:function (cp) {
        Request({method: 'GET', url: API_QUERY_URL + MARKETLIST_URL, headers: HEADERS },cp);
    },

    getTickers:function (cp) {
        Request({method: 'GET', url: API_QUERY_URL + TICKERS_URL, headers: HEADERS },cp);
    },

    getTicker:function (param,cp) {
        Request({method: 'GET', url: API_QUERY_URL + TICKER_URL + '/'+ param, headers: HEADERS },cp);
    },

    orderBooks:function (cp) {
        Request({method: 'GET', url: API_QUERY_URL + ORDERBOOKS_URL, headers: HEADERS },cp);
    },

    orderBook:function (param,cp) {
        Request({method: 'GET', url: API_QUERY_URL + ORDERBOOK_URL+  '/'+ param, headers: { 'User-Agent' : USER_AGENT } },cp);
    },

    tradeHistory:function (param,cp) {
         Request({method: 'GET', url: API_QUERY_URL + TRADEHISTORY_URL+  '/'+ param, headers: { 'User-Agent' : USER_AGENT } },cp);
    },

};

module.exports = gate;