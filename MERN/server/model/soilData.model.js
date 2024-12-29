import mongoose from "mongoose";

const soilDataSchema = new mongoose.Schema(
  {
    moistureValue: {
      type: Number,
      required: true,
    }
  },
  { timestamps: true }
);

export const SoilData = mongoose.model("SoilData", soilDataSchema);
