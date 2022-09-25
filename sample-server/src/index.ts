import express, {Application} from 'express';
import controller from './controller';
import cors from 'cors';

const PORT = process.env.PORT || '8080';
const HOST = '0.0.0.0';

const init = async () => {
    const app:Application = express();
    await controller(app);

    const options:cors.CorsOptions = {
        allowedHeaders: ['Origin'],
        origin: '*'
    };

    app.use(cors(options));
    app.use(express.json());

    app.listen(parseInt(PORT), HOST, ():void => {
        console.log(`Server Running here 👉 http://${HOST}:${PORT}`);
    });
};

init();
