var express = require('express');
var router = express.Router();

router.get('/:id',function(req,res,next){
    console.log('Router.get');
    res.send('Parameter: '+ req.params.id);
});
router.post('/', function(req, res, next){
    res.send("Title:" + req.body.title);
    console.log('Router.post');
});
router.put('/', function(req, res, next){
    res.send('PUT /');
    console.log('Router.put');
});
router.delete('/', function(req, res, next){
    res.send('Year:' + req.query.year);
    console.log('Router.delete');
});

module.exports = router;