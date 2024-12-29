import mongoose from "mongoose";

const uri = "mongodb://127.0.0.1:27017/automaticPlantWateringSystem"; 

export const dbConnection = async (params) => {
  try {
    mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    console.log(
      "Database Connection successfull!"
    );
  } catch (error) {
    console.log("Error during database Connection! ", error);
    process.exit(1);
  }
};
