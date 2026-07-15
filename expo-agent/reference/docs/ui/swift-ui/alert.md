---
title: "Alert"
description: "A SwiftUI Alert component for presenting native iOS alert dialogs."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/alert.md"
scraped_at: "2026-07-15T08:59:21.096490"
---

---
title: Alert
description: A SwiftUI Alert component for presenting native iOS alert dialogs.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Alert

A SwiftUI Alert component for presenting native iOS alert dialogs.
iOS, tvOS, Included in Expo Go

Expo UI Alert matches the official SwiftUI [alert API](https://developer.apple.com/documentation/swiftui/view/alert\(_:ispresented:actions:message:\)) and presents a native iOS alert dialog with a title, actions, and an optional message.

`Alert` is the centered modal counterpart to [`ConfirmationDialog`](/versions/latest/sdk/ui/swift-ui/confirmationdialog.md), which renders as an action sheet from the bottom of the screen. Both share the same trigger/actions/message slot model so callers can swap between them by changing the component name.

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

### Basic alert

Use `Alert.Trigger` to define the visible element and `Alert.Actions` to provide the dialog buttons.

```tsx
import { useState } from 'react';
import { Host, Alert, Button } from '@expo/ui/swift-ui';

export default function BasicAlertExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <Alert title="Saved" isPresented={isPresented} onIsPresentedChange={setIsPresented}>
        <Alert.Trigger>
          <Button label="Show alert" onPress={() => setIsPresented(true)} />
        </Alert.Trigger>
        <Alert.Actions>
          <Button label="OK" onPress={() => setIsPresented(false)} />
        </Alert.Actions>
      </Alert>
    </Host>
  );
}
```

### Cancel and confirm

Combine `role="cancel"` with a confirm button to build a standard yes/no alert.

```tsx
import { useState } from 'react';
import { Host, Alert, Button, Text } from '@expo/ui/swift-ui';

export default function CancelConfirmAlertExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <Alert title="Sign out?" isPresented={isPresented} onIsPresentedChange={setIsPresented}>
        <Alert.Trigger>
          <Button label="Sign out" onPress={() => setIsPresented(true)} />
        </Alert.Trigger>
        <Alert.Actions>
          <Button label="Sign Out" onPress={() => console.log('Signed out')} />
          <Button label="Cancel" role="cancel" />
        </Alert.Actions>
        <Alert.Message>
          <Text>You will need to sign in again to access your account.</Text>
        </Alert.Message>
      </Alert>
    </Host>
  );
}
```

### Destructive action

Use `role="destructive"` on a `Button` inside `Alert.Actions` to style it as a destructive action.

```tsx
import { useState } from 'react';
import { Host, Alert, Button, Text } from '@expo/ui/swift-ui';

export default function DestructiveAlertExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <Alert title="Delete account?" isPresented={isPresented} onIsPresentedChange={setIsPresented}>
        <Alert.Trigger>
          <Button label="Delete account" role="destructive" onPress={() => setIsPresented(true)} />
        </Alert.Trigger>
        <Alert.Actions>
          <Button
            label="Delete"
            role="destructive"
            onPress={() => {
              console.log('Deleted');
              setIsPresented(false);
            }}
          />
          <Button label="Cancel" role="cancel" />
        </Alert.Actions>
        <Alert.Message>
          <Text>This permanently deletes your account and all data. This cannot be undone.</Text>
        </Alert.Message>
      </Alert>
    </Host>
  );
}
```

## API

```tsx
import { Alert } from '@expo/ui/swift-ui';
```

## Component

### `Alert`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[AlertProps](#alertprops)\>

`Alert` presents a SwiftUI alert with a title, optional message, and action buttons.

> **See:** Official [SwiftUI documentation](https://developer.apple.com/documentation/swiftui/view/alert\(_:ispresented:actions:message:\)).

Props of the `Alert` component.

AlertProps

### `children`

Supported platforms: iOS, tvOS.

Type: `React.ReactNode`

The contents of the alert. Should include `Alert.Trigger`, `Alert.Actions`, and optionally `Alert.Message`.

### `isPresented`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean`

Whether the alert is presented.

### `onIsPresentedChange`

Supported platforms: iOS, tvOS.

Optional • Type: `(isPresented: boolean) => void`

A callback that is called when the `isPresented` state changes.

### `title`

Supported platforms: iOS, tvOS.

Type: `string`

The title of the alert.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
