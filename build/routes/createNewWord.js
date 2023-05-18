"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");
Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.createNewWordRoute = void 0;
var _regenerator = _interopRequireDefault(require("@babel/runtime/regenerator"));
var _asyncToGenerator2 = _interopRequireDefault(require("@babel/runtime/helpers/asyncToGenerator"));
var _database = require("../database");
var createNewWordRoute = {
  method: 'POST',
  path: '/api/words',
  handler: function () {
    var _handler = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee(req, h) {
      var _JSON$parse, _JSON$parse$type, type, _JSON$parse$word, word;
      return _regenerator["default"].wrap(function _callee$(_context) {
        while (1) switch (_context.prev = _context.next) {
          case 0:
            _JSON$parse = JSON.parse(req.payload), _JSON$parse$type = _JSON$parse.type, type = _JSON$parse$type === void 0 ? '' : _JSON$parse$type, _JSON$parse$word = _JSON$parse.word, word = _JSON$parse$word === void 0 ? '' : _JSON$parse$word;
            _context.next = 3;
            return _database.db.query("INSERT INTO words (id, type, word) VALUES (null, ?, ?) ", [type, word]);
          case 3:
            return _context.abrupt("return", {
              type: type,
              word: word
            });
          case 4:
          case "end":
            return _context.stop();
        }
      }, _callee);
    }));
    function handler(_x, _x2) {
      return _handler.apply(this, arguments);
    }
    return handler;
  }()
};
exports.createNewWordRoute = createNewWordRoute;