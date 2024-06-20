MONGO_URI needs to be configure like this `MONGO_URI='mongodb://admin:admin@mongodb:27017'`
./public/product-images will be store the images
`shopping` will be the db name 

# to run and test 
docker run -dit --name nodewebapp -p 3030:3000 -e MONGO_URI='mongodb://admin:admin@mongodb:27017' --network apps-network  vishalvijayakumarv/nodewebapp:0.0.1

# volume set with `/app/public/product-images` path for store data


# To create a user with access the db 
db.createUser(
  {
    user: "admin",
    pwd: "admin",
    roles: [ { role: "readWrite", db: "shopping" } ]
 }
)
