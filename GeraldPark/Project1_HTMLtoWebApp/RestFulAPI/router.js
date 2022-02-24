var express = require('express');
var router = express.Router();

router.get('/:id',function(req,res,next){
    res.send('Parameter: '+ req.params.id);
});
router.post('/', function(req, res, next){
    res.send("Title:" + req.body.title);
});
router.put('/', function(req, res, next){
    res.send('PUT /');
});
router.delete('/', function(req, res, next){
    res.send('Year:' + req.query.year);
});

module.exports = router;