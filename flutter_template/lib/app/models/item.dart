class Item {
  /// id
  int? _id;

  /// 이름
  String? _name;

  /// 설명
  String? _description;

  /// 가격
  double? _price;

  /// 사용 유무
  bool? _isAvailable;

  Item({
    int? id,
    String? name,
    String? description,
    double? price,
    bool? isAvailable,
  }) {
    if (id != null) {
      this._id = id;
    }
    if (name != null) {
      this._name = name;
    }
    if (description != null) {
      this._description = description;
    }
    if (price != null) {
      this._price = price;
    }
    if (isAvailable != null) {
      this._isAvailable = isAvailable;
    }
  }

  int? get id => _id;
  set id(int? id) => _id = id;
  String? get name => _name;
  set name(String? name) => _name = name;
  String? get description => _description;
  set description(String? description) => _description = description;
  double? get price => _price;
  set price(double? price) => _price = price;
  bool? get isAvailable => _isAvailable;
  set isAvailable(bool? isAvailable) => _isAvailable = isAvailable;

  Item.fromJson(Map<String, dynamic> json) {
    _id = json['id'];
    _name = json['name'];
    _description = json['description'];
    _price = json['price'];
    _isAvailable = json['is_available'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this._id;
    data['name'] = this._name;
    data['description'] = this._description;
    data['price'] = this._price;
    data['is_available'] = this._isAvailable;
    return data;
  }
}
