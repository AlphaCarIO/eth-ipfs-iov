pragma solidity ^0.4.21;

import "zeppelin-solidity/contracts/ownership/Ownable.sol";
import "zeppelin-solidity/contracts/math/SafeMath.sol";
import "../utils/StringUtils.sol";

contract IOVContract is Ownable {

    using SafeMath for uint;
    using StringUtils for string;

    struct IOVInfo {
        string hashVal;
        uint timestamp;
        
        bool flag;
    }

    event NewHashAdded(IOVInfo _info);

    uint public count = 0;
    
    string[] datetimes;

    mapping(string => IOVInfo) infos;

    modifier notOwner() {
        require(msg.sender != owner);
        _;
    }

    function IOVContract() public {
    }
    
    /*
    function compareStrings(string a, string b) internal pure returns (bool) {
       return keccak256(a) == keccak256(b);
    }*/

    function storeHash(string _datetime, string _hashVal) public onlyOwner {
        //require(!compareStrings(_datetime, "") && !compareStrings(_hashVal, ""));
        require(!_datetime.equal("") && !_hashVal.equal(""));

        IOVInfo memory info = IOVInfo({hashVal: _hashVal, timestamp: now, flag: true});
        infos[_datetime] = info;
        datetimes.push(_datetime);

        count = count.add(1);

        emit NewHashAdded(info);
    }

    function getTimestamp(string _datetime) public view returns (uint) {
        if (infos[_datetime].flag) {
            IOVInfo memory info = infos[_datetime];
            return info.timestamp;
        }
        return 0;
    }

    function getHash(string _datetime) public view returns (string) {
        if (infos[_datetime].flag) {
            IOVInfo memory info = infos[_datetime];
            return info.hashVal;
        }
        return "";
    }

    function getDateTime(uint _count) public view returns (string) {
        require(_count < count);
        return datetimes[_count];
    }

    function currentDateTime() public view returns (string) {
        if (count == 0) {
            return "";
        }
        return datetimes[count - 1];
    }

}
