---
title: "Button"
description: "A SwiftUI Button component for displaying native buttons."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/button.md"
scraped_at: "2026-07-15T08:59:43.393212"
---

---
title: Button
description: A SwiftUI Button component for displaying native buttons.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Button

A SwiftUI Button component for displaying native buttons.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Button`](/versions/latest/sdk/ui/universal/button.md) — it renders the appropriate native component per platform.

Expo UI Button matches the official SwiftUI [Button API](https://developer.apple.com/documentation/swiftui/button) and supports styling via the [`buttonStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#buttonstylestyle), [`controlSize`](/versions/latest/sdk/ui/swift-ui/modifiers.md#controlsizesize), and other modifiers.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic button

```tsx
import { Host, Button } from '@expo/ui/swift-ui';

export default function BasicButtonExample() {
  return (
    <Host matchContents>
      <Button label="Press me" onPress={() => alert('Pressed!')} />
    </Host>
  );
}
```

### Button with system image

```tsx
import { Host, Button } from '@expo/ui/swift-ui';

export default function ButtonWithImageExample() {
  return (
    <Host matchContents>
      <Button
        label="Download"
        systemImage="arrow.down.circle"
        onPress={() => alert('Downloading...')}
      />
    </Host>
  );
}
```

### Icon-only button

Use the `labelStyle` modifier to show only the icon while keeping the label for accessibility.

```tsx
import { Host, Button } from '@expo/ui/swift-ui';
import { labelStyle } from '@expo/ui/swift-ui/modifiers';

export default function IconOnlyButtonExample() {
  return (
    <Host matchContents>
      <Button
        label="Settings"
        systemImage="gear"
        modifiers={[labelStyle('iconOnly')]}
        onPress={() => alert('Settings')}
      />
    </Host>
  );
}
```

### Button styles

Use the `buttonStyle` modifier to change the button's appearance. Available styles are: `bordered`, `borderedProminent`, `borderless`, `plain`, `glass`, and `glassProminent`.

> **Note:** The `glass` and `glassProminent` styles are only available on iOS 26+ when built with Xcode 26.

```tsx
import { Host, Button, VStack } from '@expo/ui/swift-ui';
import { buttonStyle } from '@expo/ui/swift-ui/modifiers';

export default function ButtonStylesExample() {
  return (
    <Host matchContents>
      <VStack spacing={8}>
        <Button label="Bordered" modifiers={[buttonStyle('bordered')]} />
        <Button label="Bordered Prominent" modifiers={[buttonStyle('borderedProminent')]} />
        <Button label="Borderless" modifiers={[buttonStyle('borderless')]} />
        <Button label="Plain" modifiers={[buttonStyle('plain')]} />
      </VStack>
    </Host>
  );
}
```

### Button border shape

Use the `buttonBorderShape` modifier to change the shape of a styled button. Available shapes are: `automatic`, `capsule`, `roundedRectangle`, and `circle` (iOS 17+).

```tsx
import { Host, Button } from '@expo/ui/swift-ui';
import {
  buttonStyle,
  controlSize,
  buttonBorderShape,
  labelStyle,
} from '@expo/ui/swift-ui/modifiers';

export default function ButtonBorderShapeExample() {
  return (
    <Host matchContents>
      <Button
        label="Favorite"
        systemImage="heart.fill"
        modifiers={[
          buttonStyle('glass'),
          controlSize('extraLarge'),
          labelStyle('iconOnly'),
          buttonBorderShape('circle'),
        ]}
        onPress={() => alert('Favorited')}
      />
    </Host>
  );
}
```

### Control sizes

Use the `controlSize` modifier to adjust the button size. Available sizes are: `mini`, `small`, `regular`, `large`, and `extraLarge`.

> **Note:** The `extraLarge` size is only available on iOS 17+.

```tsx
import { Host, Button, VStack } from '@expo/ui/swift-ui';
import { buttonStyle, controlSize } from '@expo/ui/swift-ui/modifiers';

export default function ControlSizeExample() {
  return (
    <Host matchContents>
      <VStack spacing={8}>
        <Button label="Mini" modifiers={[controlSize('mini'), buttonStyle('bordered')]} />
        <Button label="Small" modifiers={[controlSize('small'), buttonStyle('bordered')]} />
        <Button label="Regular" modifiers={[controlSize('regular'), buttonStyle('bordered')]} />
        <Button label="Large" modifiers={[controlSize('large'), buttonStyle('bordered')]} />
      </VStack>
    </Host>
  );
}
```

### Button roles

Use the `role` prop to indicate the semantic role of the button. Available roles are: `default`, `cancel`, and `destructive`.

```tsx
import { Host, Button, VStack } from '@expo/ui/swift-ui';

export default function ButtonRolesExample() {
  return (
    <Host matchContents>
      <VStack spacing={8}>
        <Button label="Default" role="default" />
        <Button label="Cancel" role="cancel" />
        <Button label="Delete" role="destructive" />
      </VStack>
    </Host>
  );
}
```

### Tinted button

Use the `tint` modifier to change the button's color.

```tsx
import { Host, Button } from '@expo/ui/swift-ui';
import { tint } from '@expo/ui/swift-ui/modifiers';

export default function TintedButtonExample() {
  return (
    <Host matchContents>
      <Button label="Custom Color" modifiers={[tint('#FF6347')]} />
    </Host>
  );
}
```

### Disabled button

Use the `disabled` modifier to disable the button.

```tsx
import { Host, Button } from '@expo/ui/swift-ui';
import { disabled } from '@expo/ui/swift-ui/modifiers';

export default function DisabledButtonExample() {
  return (
    <Host matchContents>
      <Button label="Disabled" modifiers={[disabled()]} />
    </Host>
  );
}
```

### Custom label content

You can pass custom components as `children` for more complex button label content.

```tsx
import { Host, Button, VStack, Image, Text } from '@expo/ui/swift-ui';

export default function CustomContentExample() {
  return (
    <Host matchContents>
      <Button onPress={() => console.log('Pressed!')}>
        <VStack spacing={4}>
          <Image systemName="folder" />
          <Text>Folder</Text>
        </VStack>
      </Button>
    </Host>
  );
}
```

## API

```tsx
import { Button } from '@expo/ui/swift-ui';
```

## Component

### `Button`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

Displays a native button component.

Example

```tsx
import { Button } from '@expo/ui/swift-ui';
import { buttonStyle, controlSize, tint, disabled } from '@expo/ui/swift-ui/modifiers';

<Button
  role="destructive"
  onPress={handlePress}
  label="Delete"
  modifiers={[
    buttonStyle('bordered'),
    controlSize('large'),
    tint('#FF0000'),
    disabled(true)
  ]}
/>
```

ButtonProps

### `children`

Supported platforms: iOS, tvOS.

Optional • Literal type: `union`

Custom content for the button label. Use this for custom label views. Only nested elements are supported, not plain strings.

Acceptable values are: `ReactElement<unknown, string | JSXElementConstructor<any>>` | `ReactElement[]`

### `label`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

The text label for the button. Use this for simple text buttons.

### `onPress`

Supported platforms: iOS, tvOS.

Optional • Type: `() => void`

A callback that is called when the button is pressed.

### `role`

Supported platforms: iOS, tvOS.

Optional • Type: [ButtonRole](#buttonrole)

Indicates the role of the button.

### `systemImage`

Supported platforms: iOS, tvOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

A string describing the system image to display in the button. Only used when `label` is provided.

### `target`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

Target identifier for the button, used for identifying which button was pressed in widgets and live activities.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

## Types

### `ButtonRole`

Supported platforms: iOS, tvOS.

Literal Type: `string`

The role of the button.

-   `default` - The default button role.
-   `cancel` - A button that cancels the current operation.
-   `destructive` - A button that deletes data or performs a destructive action.

Acceptable values are: `'default'` | `'cancel'` | `'destructive'`
