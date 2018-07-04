import * as mongowrapper from '../utils/mongowrapper'

var BigNumber = require('bignumber.js')
BigNumber.config({
  DECIMAL_PLACES: 18
})

export async function latestUBIInfo(ctx) {
  let res = await mongowrapper.UBIInfoModel.find({})
    .sort('-timestamp')
    .select({
      _id: 0
    })
    .limit(1)
    .exec()

  let error_code = -1;
  let error_msg = 'no data';
  let data = {};

  if (res.length > 0) {
    error_code = 0;
    error_msg = "";
    data = res[0];
  }

  let body = {
    'error_code': error_code,
    'error_msg': error_msg,
    data: data
  }

  ctx.response.body = body
}

export async function getUBIInfoByCode(ctx) {
  let ubi_code = ctx.params.ubi_code
  let res = await mongowrapper.UBIInfoModel.find({
      'ubi_code': ubi_code
    })
    .sort('-timestamp')
    .select({
      _id: 0
    })
    .limit(1)
    .exec()

  let error_code = -1;
  let error_msg = 'no data';
  let data = {};

  if (res.length > 0) {
    error_code = 0;
    error_msg = "";
    data = res[0];
  }

  let body = {
    'error_code': error_code,
    'error_msg': error_msg,
    data: data
  }

  ctx.response.body = body
}

export async function getUBIInfoList(ctx) {
  var param = ctx.request.query;
  let search_type = param['search_type']
  let search_txt = param['search_txt']

  let cond = {}

  var opt_lst = ['1', '2', '3', '4'];

  if (search_type == undefined || search_type == '' || opt_lst.indexOf(search_type) == -1) {
    search_type = '0'
  }

  console.log('search_type:', search_type, ' search_txt:', search_txt)

  if (search_txt == undefined || search_txt == '') {
  } else if (search_type == '0') {
    cond = {
      '$or': [{
          'ubi_code': search_txt
        },
        {
          'car_info.vin_code': search_txt
        },
        {
          'user.driving_license': search_txt
        },
        {
          'user.name': search_txt
        },
      ]
    }
  } else if (search_type == '1') {
    cond = {
      'ubi_code': search_txt
    }
  } else if (search_type == '2') {
    cond = {
      'car_info.vin_code': search_txt
    }
  } else if (search_type == '3') {
    cond = {
      'user.name': search_txt
    }
  } else if (search_type == '4') {
    cond = {
      'user.driving_license': search_txt
    }
  }

  console.log('cond', cond)

  let res = await mongowrapper.UBIInfoModel.find(cond)
    .sort('-timestamp')
    .select({
      _id: 0
    })
    .exec()

  let error_code = 0;
  let error_msg = '';

  let body = {
    'error_code': error_code,
    'error_msg': error_msg,
    data: res
  }

  ctx.response.body = body
}