const EVENT_HAS_ERROR = "HAS_ERROR";
const EVENT_MENU_CHANGED = "MENU_CHANGED";
const TIME_TO_CHECK = 500;

const CHROME_METAMASK = 'https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?utm_campaign=en&utm_source=en-et-na-us-oc-webstrext&utm_medium=et';
const FIREFOX_METAMASK = 'https://addons.mozilla.org/zh-CN/firefox/addon/ether-metamask';

const MESSAGE_NOT_CONNECTED = "未连接以太坊账户!";
const MESSAGE_NO_METAMASK = "未安装MetaMask扩展程序!";
const MESSAGE_NO_NETWORK = "不能解析网络ID!";
const MESSAGE_NO_COINBASE = "不能解析COINBASE!";
const MESSAGE_NO_BALANCE = "无法获取账户金额!";
const MESSAGE_INVALID_CONTRACT_ADDRESS = "错误的合约地址!";

module.exports = {
    EVENT_HAS_ERROR,
    EVENT_MENU_CHANGED,
    TIME_TO_CHECK,
    CHROME_METAMASK,
    FIREFOX_METAMASK,
    MESSAGE_NOT_CONNECTED,
    MESSAGE_NO_METAMASK,
    MESSAGE_NO_NETWORK,
    MESSAGE_NO_COINBASE,
    MESSAGE_NO_BALANCE,
    MESSAGE_INVALID_CONTRACT_ADDRESS,
}
