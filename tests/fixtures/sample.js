/** A small counter widget. */
export class CounterWidget extends Component {
    setup() {
        this.state = 0;
    }
    increment() {
        this.state += 1;
    }
}

function formatValue(v) {
    return `Value: ${v}`;
}

const double = (x) => x * 2;
