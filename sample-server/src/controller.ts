import {Request, Response, Application} from 'express';
import { area, restaurant } from './types';
import AreaData from './area.json';
import RestaurantData from './restaurant.json';

const controller = (app: Application) => {
    app.get("/", (req:Request, res:Response):void => {
        res.send("Hello Typescript with Node.js!")
    });

    app.get("/areas", (req:Request, res:Response):void => {
        res.header("Access-Control-Allow-Origin", "*")
        res.send({'areas': AreaData.areas as Array<area>});
    });

    app.get("/areas/:id/restaurants", (req: Request, res:Response):void => {
        let restaurants = RestaurantData.restaurants as Array<restaurant>;
        let filteredByArea: restaurant[] = [];
        restaurants.forEach(restaurant => {
            if (restaurant.areaId === req.params['id']) {
                filteredByArea.push(restaurant);
            }
        });
        res.send({'restaurants': filteredByArea});
    });
};

export default controller;