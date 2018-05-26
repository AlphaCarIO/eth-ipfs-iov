function BaseOperation() {
    
    this.getDB = function() {
        conn = new Mongo();
        let db = conn.getDB("alphacar");
        //db.auth("user-name","password");
        return db;
    }
}
