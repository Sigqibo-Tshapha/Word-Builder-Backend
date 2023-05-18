"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");
var _regenerator = _interopRequireDefault(require("@babel/runtime/regenerator"));
var _asyncToGenerator2 = _interopRequireDefault(require("@babel/runtime/helpers/asyncToGenerator"));
var _hapi = _interopRequireDefault(require("@hapi/hapi"));
var _routes = _interopRequireDefault(require("./routes"));
var _database = require("./database");
var _dotenv = _interopRequireDefault(require("dotenv"));
_dotenv["default"].config();
var server;
var start = /*#__PURE__*/function () {
  var _ref = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee() {
    var server;
    return _regenerator["default"].wrap(function _callee$(_context) {
      while (1) switch (_context.prev = _context.next) {
        case 0:
          server = _hapi["default"].server({
            port: 8080,
            host: 'localhost'
          });
          _database.db.connect();
          _routes["default"].forEach(function (route) {
            return server.route(route);
          });
          _context.next = 5;
          return server.start();
        case 5:
          console.log("Server is listening on  ".concat(server.info.uri));
        case 6:
        case "end":
          return _context.stop();
      }
    }, _callee);
  }));
  return function start() {
    return _ref.apply(this, arguments);
  };
}();
process.on('unhandledRejection', function (err) {
  console.log(err);
  process.exit(1);
});
start();