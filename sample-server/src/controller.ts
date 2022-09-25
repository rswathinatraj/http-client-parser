import {Request, Response, Application} from 'express';
import { area } from './types';
import AreaData from './area.json';

const controller = (app: Application) => {
    app.get("/", (req:Request, res:Response):void => {
        res.send("Hello Typescript with Node.js!")
    });

    app.get("/areas", (req:Request, res:Response):void => {
        res.header("Access-Control-Allow-Origin", "*")
        res.send({'areas': AreaData.areas as Array<area>});
    });
};

export default controller;