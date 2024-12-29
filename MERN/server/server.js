import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import { SoilData } from "./model/soilData.model.js";
import { dbConnection } from "./db/dbConnection.js";
dbConnection();

const app = express();
app.use(bodyParser.json());
app.use(cors());

app.post("/soil-data", async (req, res) => {
  const { moistureValue } = req.body;
  console.log("Received Moisture Value:", moistureValue);
  //saving moisture value in database
  const data = new SoilData({ moistureValue });
  await data.save();
  res.status(200).send("Data Received");
});

app.get("/get-soil-data", async (req, res) => {
  // Fetch all moisture data from the database
  const soilData = await SoilData.find();
  // Send the data as the response
  res.status(200).json(soilData);
});

app.listen(3000, () => console.log("Server running on port 3000"));
